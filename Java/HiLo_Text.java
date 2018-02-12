import java.util.Scanner;

class HiLo_Text {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String playAgain = "";
		do {
			int num = (int)(Math.random() * 100 + 1);
			int guess = 0;
			while (guess != num) {
				System.out.println("Guess a number between 1 and 100:");
				guess = scan.nextInt();
				if (guess < num)
					System.out.println(guess + " is too low. Try again");
				else if (guess > num)
					System.out.println(guess + " is too high. Try again");
				else
					System.out.println(guess +" is correct. You Win!");
			}
			System.out.println("Would you like to play again? (y/n)");
			playAgain = scan.next();
		} while (playAgain.equalsIgnoreCase("y"));
		System.out.println("Thanks for playing");
		scan.close();
	}
}