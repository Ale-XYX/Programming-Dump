import javax.swing.*;

class Window_Test {
	public static void main(String[] args) {
		JFrame frame = new JFrame("Hello World!");
		JPanel panel = new JPanel();
		JButton button = new JButton("Click me!");

		panel.add(button);
		frame.add(panel);
		frame.setSize(300, 100);
		button.addActionListener(e ->
			System.out.println("Ouch! You Clicked me!"));
		frame.setVisible(true);
	}
}