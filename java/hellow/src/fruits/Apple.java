package fruits;

public class Apple extends Fruit {
	
	String color ;
	public Apple () {
		super();
		this.color = "Red";
	}
	
	public void display () {
		System.out.println("Printing the characteristics of a Apple");
		System.out.println(this.weight);
		System.out.println(this.color);
	}

}
