public class Goose extends Pet {

    public Goose (String name){
        setSpecies("Goose");
        setName(name);
    }

    @Override
    public void makeSound() { //Override: Sets sound to "quack!"
        System.out.println("honk!");
    }
}
