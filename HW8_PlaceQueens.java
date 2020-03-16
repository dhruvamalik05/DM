/**********
* Name:Dhruva Malik
* File:Homework8 PlaceQueens
* Desc:takes various inputs and accordingly does function with a queen and also make the table of desired size
* some of the options are like make, delete, add, reset, and quit.
***********/
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
public class HW8_PlaceQueens{
 public static String[][] make_board(int size){
 String[][] board = new String [size][size];
 for (int z= 0 ;  z<size; z++){
   Arrays.fill(board[z],"   ");

 }
 return board;
  }
 public static void print_board(String[][] board){
 String dash = "";
 for (int y= 0 ;y<(4*(board.length+1)); y++){
 dash = dash + "-";
 }
 
for (int x= 0 ; x<=board.length ; x++){
if (x == 0){
System.out.printf("   |");
}
else{
 System.out.printf("%3d|",x);
}
}
System.out.printf("%n%s%n",dash.substring(1));

 for (int i = 0 ; i<board.length ; i++){
 System.out.printf("%3d|",(i+1));
  for (int u = 0 ; u<board.length ; u++){
 
 System.out.printf("%s|",board[i][u]);
 }
 System.out.printf("%n%s%n",dash);
 }
 }
 public static void reset_board(String[][] board){
 for (int z= 0 ;  z<board.length; z++){
   Arrays.fill(board[z],"   ");

 }
  }
  public static void add_queen (int a, int b, String[][] board){
  
  for (int x=0 ; x<board.length; x++){
  
  if ((a-x-1)>=0&&(b-x-1)>=0&&(a-x-1)<board[0].length&&(b-x-1)<board.length&&(!(board[a-x-1][b-x-1].equals(" Q ")))){
  board[a-x-1][b-x-1]=" * ";
  }
  
  if ((a-x-1)>=0&&(b+x-1)>=0&&(a-x-1)<board[0].length&&(b+x-1)<board.length&&(!(board[a-x-1][b+x-1].equals(" Q ")))){
  board[a-x-1][b+x-1]=" * ";
  }
  
  if ((a+x-1)>=0&&(b-x-1)>=0&&(a+x-1)<board[0].length&&(b-x-1)<board.length&&(!(board[a+x-1][b-x-1].equals(" Q ")))){
  board[a+x-1][b-x-1]=" * ";
  
  }
  if ((a+x-1)>=0&&(b+x-1)>=0&&(a+x-1)<board[0].length&&(b+x-1)<board.length&&(!(board[a+x-1][b+x-1].equals(" Q ")))){
  board[a+x-1][b+x-1]=" * ";
 
  }
  if ((a-1-x)>=0&&(a-1-x)<board.length&&(!(board[a-x-1][b-1].equals(" Q ")))){
  board[a-1-x][b-1]=" * ";
  
  }
   if ((b-1-x)>=0&&(b-1-x)<board.length&&(!(board[a-1][b-x-1].equals(" Q ")))){
   board[a-1][b-1-x]=" * ";
  }
  
  if ((a-1+x)>=0&&(a-1+x)<board.length&&(!(board[a+x-1][b-1].equals(" Q ")))){
  board[a-1+x][b-1]=" * ";
  
  }
  if ((b-1+x)>=0&&(b-1+x)<board.length&&(!(board[a-1][b+x-1].equals(" Q ")))){
  board[a-1][b-1+x]=" * ";
  
  }
  board[a-1][b-1]=" Q ";
  }
  }
 
  public static int count_queens (String[][] board){
  int z=0;
  for (int i =0 ; i <board.length; i++){
   for (int y = 0 ; y < board.length; y++){
   if ( board[i][y].equals(" Q ")){
   z++;
   }
   }
  }
  return z;
  }
  /*public static void delete_queen (int a , int b , String[][] board){(delete queens by array lists)
  ArrayList<Integer> place_queens = new ArrayList<Integer>();
  for (int i =0; i < board.length ; i++){
  for ( int x = 0 ; x< board.length ; x++){
   if (board[i][x].equals(" Q ")){
   place_queens.add(i);
   place_queens.add(x);
    }
   }
  }
  int size = place_queens.size()/2 ;
  for (int y= 0 ; y<size; y++){
  if ((a==place_queens.get(2*y))&&(b==place_queens.get((2*y)+1))){
  place_queens.remove((2*y)+1);
  place_queens.remove(2*y);
  }
  }
   reset_board(board);
   //for (int z= 0 ;  z<board.length; z++){
   //Arrays.fill(board[z],"   ");}

  for (int m= 0 ; m<((place_queens.size())/2);m++){
  add_queen(place_queens.get(2*m),place_queens.get((2*m)+1),board);
  }
  
  }*/
  public static void delete_queen (int a , int b, String[][] board){
 // for (int check1 =0 ; check1<board.length ; check1++){for (int check2 =0 ; check2<board.length ; check2++){
   if (!(board[a-1][b-1].equals(" Q "))){
      System.out.printf("queen not present at this location%n");
  }
  else
  {
  int x = count_queens(board);
  int e = 0 ;
  int [][] place_queens = new int[2][x];
  for (int i =0 ; i<(board.length); i++)
  {  // rows
      for(int u = 0 ; u<(board.length); u++)
      { // col
            if (board[i][u].equals(" Q "))
            {
                  //if (i+1 != a && u+1 != b)
                  //{
                        place_queens[0][e]=i;
                        place_queens[1][e]=u;
                        e++;
                  //}                  
             }
       }
  }
  
  reset_board(board);

  for (int y= 0 ; y<x; y++){
      if (!(place_queens[0][y] == a-1 && place_queens[1][y] == b-1)) 
         add_queen((place_queens[0][y]+1),(place_queens[1][y]+1),board);
      
  }
  
  //q
 // print_board(board);
  }
  }

  
 public static void main(String[] args){
 Scanner choice = new Scanner (System.in);
  Scanner num = new Scanner (System.in);
 int size = 0;
 int counter = 0 ;
 String[][] board = make_board(size);

 while (counter==0){
// String[][] board = make_board(size);
  System.out.printf("q - quit%nr - reset,%nm - make,%na - add queen,%nd - delete queen,%nc - count queen,%np - print board%n");
  System.out.printf("Enter option:");
  String l1 = choice.nextLine().toLowerCase();
  if (l1.equals("q")){
  System.out.printf("Good Bye!");
  counter++;
  }
  if (l1.equals("r")){
  if (size==0){
   System.out.printf("error ! size not available%n");
  }
  else{
  //board = make_board(size);
  reset_board(board);
  print_board(board);
  }
  }
  if(l1.equals("m")){
  System.out.printf("Enter board size:%n");
  size = num.nextInt(); 
  board  = make_board(size);
  print_board(board);
  }
  if(l1.equals("a")){
   if (size==0){
   System.out.printf("error ! size not available%n");
  }
  else{

  System.out.printf("Enter row and column (1-N):");
  int row = num.nextInt();
  int col = num.nextInt();
   // board = make_board(size);

  add_queen(row,col,board);
  print_board(board);
  }
  }
  if (l1.equals("d")){
   if (size==0){
   System.out.printf("error ! size not available%n");
  }
  else{

  System.out.printf("Enter row and column (1-N):");
  int row= num.nextInt();
  int col = num.nextInt();
   // board = make_board(size);

  delete_queen(row,col,board);
  print_board(board);
  }}
  if (l1.equals("c")){
   if (size==0){
   System.out.printf("error ! size not available%n");
  }
  else{

    //board = make_board(size);
  System.out.printf("Counted queens on board:%d%n",count_queens(board));
  }}
  if (l1.equals("p")){
  System.out.printf("Not a valid board. Cannot be printed.%n");
  }
 }
 //System.exit(0);
  /*String[][] yo = make_board(8);
  add_queen(4,4,yo);  add_queen(6,4,yo);

  print_board(yo);
  System.out.printf("%d%n%n%n",count_queens(yo));
    reset_board(yo);
    print_board(yo)  ;
    add_queen(4,5,yo);
    add_queen(4,4,yo);    print_board(yo)  ;
      System.out.printf("%d%n%n%n",count_queens(yo));


  delete_queen(4,4,yo);
    print_board(yo);
      System.out.printf("%d%n%n%n",count_queens(yo));

    add_queen(3,3,yo);
    print_board(yo);
  System.out.printf("%d%n%n%n",count_queens(yo));*/
 }
}