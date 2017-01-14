package prob022;

import java.io.File;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class prob022
{
   public static void main(String[] args) throws Exception
   {
      File file = new File("p022_names.txt");
      Scanner input = new Scanner(file);
      String[] names = input.next().split(",");
      Arrays.sort(names);
      
      BigInteger sum = BigInteger.ZERO;
      int nameSum = 0;
      String cName;
      for (int i = 0; i < names.length; i++)
      {
         cName = names[i];
         nameSum = 0;
         
         // ignore the " at first and last
         for (int j = 1; j < cName.length() - 1; j++)
            nameSum += (int) cName.charAt(j) - 64;
         
         sum = sum.add(BigInteger.valueOf(nameSum * (i+1)));
      }
      
      System.out.println("finally " + sum);
   }
   
}
