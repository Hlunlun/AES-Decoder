import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

import java.io.*;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;


class Decode{
    public static void main(String[] args) throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, IllegalBlockSizeException, BadPaddingException, IOException  {
        
        String cipher = "2NHkjlDyk82JBke5q8CnMQZ1iiHID8QEst+/Ld6lWFMP5omXXh/1LnmrYKOD04idKfzfL+6C96391/iN7+X0eg==";
        
        String samples = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";

        FileWriter result = new FileWriter("results.txt");
        PrintWriter out = new PrintWriter(result);

        for(int i=0;i<samples.length();i++){
            for(int j=0;j<samples.length();j++){
                for(int k=0;k<samples.length();k++){
                    for(int l=0;l<samples.length();l++){
                        String key = "$\""+ samples.charAt(i) + "vXl" + samples.charAt(j) + "K" + samples.charAt(k)+"\\/{9Fp"+samples.charAt(l);
                        SecretKeySpec keySpec = new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), "AES");
                        Cipher aes = Cipher.getInstance("AES/ECB/NoPadding");
                        aes.init(Cipher.DECRYPT_MODE, keySpec);
                        byte[] byte_plaintext = aes.doFinal(Base64.getDecoder().decode(cipher));
                        String plaintext = new String(byte_plaintext, StandardCharsets.UTF_8);
                        
                        if(plaintext.matches("[a-zA-Z0-9  !\"#$%&\'()*+,-.@/:;\\[\\]{|}~\0]{1,}")){
                            String write = "\n -------------------------------------------\n key: "+key+"\n plaintext: "+plaintext+"\n";
                            out.println(write);
                            out.flush();
                            out.close();
                            System.out.println("key: "+key);
                            System.out.println(plaintext);
                        }                  
                    }
                }
            }
        }
        result.close();
    }

}