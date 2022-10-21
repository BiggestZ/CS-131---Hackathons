public class ExampleMain {

    public static void main(String[] args) {
        // create a new empty library
        Library lib = new Library();

        // add some items to the library's collection
        lib.addToCollection(new Book("Pride and Prejudice", "Jane Austen"));
        lib.addToCollection(new Book("Perks of Being a Wallflower", "Stephen Chbosky"));
        lib.addToCollection(new Film("Wonder", "Stephen Chbosky"));
        lib.addToCollection(new Film("Wonder Woman", "Patty Jenkins"));
        lib.addToCollection(new Book("Breaking Dawn", "Stephenie Meyer"));
        lib.addToCollection(new Book("Frankenstein", ""));

        // print the collection
        lib.printCollection();
        System.out.println();

        // search for items by various creators

        int num_chbosky = lib.countCreatorItems("Stephen Chbosky");
        System.out.println("There are " + num_chbosky + " works by Stephen Chbosky in the library.");

        int num_austen = lib.countCreatorItems("Jane Austen");
        System.out.println("There are " + num_austen + " works by Jane Austen in the library.");

        int num_king = lib.countCreatorItems("Stephen King");
        System.out.println("There are " + num_king + " works by Stephen King in the library.");
    }

}