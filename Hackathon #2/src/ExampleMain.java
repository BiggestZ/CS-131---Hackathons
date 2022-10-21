//import java.util.ArrayList;
public class ExampleMain {

    public static void main(String[] args) {
        PetHotel redWoofInn = new PetHotel(3);

        redWoofInn.numRoomsAvailable(); // 3

        Duck huey = new Duck("Huey");
        redWoofInn.checkIn(huey); // true;
        huey.makeSound(); // prints "quack!"

        Duck dewey = new Duck("Dewey");
        redWoofInn.checkIn(dewey); // true;
        dewey.makeSound(); // prints "quack!"

        Duck louie = new Duck("Louie");
        redWoofInn.checkIn(louie); // true;
        louie.makeSound(); // prints "quack!"

        redWoofInn.numRoomsAvailable(); // 0

        Goose mother = new Goose("Mother");
        redWoofInn.checkIn(mother); // returns false;
        mother.makeSound(); // prints "honk!"

        redWoofInn.getRoomOf(dewey); // 1
        redWoofInn.getOccupantOf(1).getName(); // "Dewey" 

        redWoofInn.checkOut(mother); // false
        redWoofInn.checkOut(louie); // true

        redWoofInn.numRoomsAvailable(); // 1

        Pet edgar = new Pet("cockroach", "Edgar");
        redWoofInn.checkIn(edgar); // true
        edgar.makeSound(); // prints "I love the Beach Boys!"

        redWoofInn.checkOut(huey); // true
        redWoofInn.checkOut(dewey); // true

        System.out.println("Roaches check in...");
        System.out.println("...they don't check out.");
    }
}
