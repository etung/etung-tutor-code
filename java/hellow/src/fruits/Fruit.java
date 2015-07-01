package fruits;

public class Fruit {
	int weight;
	
	public Fruit () {
		this.weight = 0;
	}
	
	public Fruit (int weight) {
		this.weight = weight;
	}
	
	public void display () {
		System.out.println("Printing the characteristics of a Fruit");
		System.out.println(this.weight);
	}

}
