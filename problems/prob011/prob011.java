package prob011;

import java.io.File;
import java.util.Scanner;

public class prob011
{
   static final String filePath = "p011.txt";
   static int[][] grid = new int[20][20];
   
   public static void main(String[] args) throws Exception
   {
      File file = new File(filePath);
      Scanner scan = new Scanner(file);
      
      for (int i = 0; i < grid.length; i++)
      {
         String[] strList = scan.nextLine().split(" ");
         for (int j = 0; j < strList.length; j++)
            grid[i][j] = Integer.parseInt(strList[j]);
      }
      
      long max_p = 0;
      
      for (int i = 0; i < grid.length - 3; i++)
         for (int j = 0; j < grid[i].length; j++)
         {
            long product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j];
            if (product > max_p)
               max_p = product;
         }
      
      for (int i = 0; i < grid.length; i++)
         for (int j = 0; j < grid[i].length - 3; j++)
         {
            long product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3];
            if (product > max_p)
               max_p = product;
         }
      
      for (int i = 0; i < grid.length - 3; i++)
         for (int j = 0; j < grid[i].length - 3; j++)
         {
            long product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3];
            if (product > max_p)
               max_p = product;
         }
      
      for (int i = 0; i < grid.length - 3; i++)
         for (int j = 3; j < grid[i].length; j++)
         {
            long product = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3];
            if (product > max_p)
               max_p = product;
         }
      
      System.out.println("finally " + max_p);
   }
}
