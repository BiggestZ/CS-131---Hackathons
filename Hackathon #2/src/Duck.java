public class Duck extends Pet {

    public Duck(String name){ // Constructor for all Ducks
        setSpecies("Duck");
        setName(name);  
    }

    @Override
    public void makeSound() { //Override: Sets sound to "quack!"
        System.out.println("quack!");
    }
    
}
