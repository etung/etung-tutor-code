package fruits;

import fruits.Apple;
import fruits.Fruit;

public class UnitTest {
	public static void main (String args[]) {
		Apple apple = new Apple();
		apple.display();
		((Fruit)apple).display();
	}

}
