import java.util.ArrayList;

public class Library {
    private ArrayList<LibraryItem> pup  = new ArrayList<LibraryItem>();
    /* Constructor; creates an empty collection.
     */

    public Library() {
    }

    /* Add a LibraryItem to the collection
     *
     * @param obj  The item to add.
     */
    public void addToCollection(LibraryItem obj) {
        pup.add(obj);
    }

    /* Count the number of items by the specified creator.
     *
     * The creator must match exactly.
     *
     * @param creator  The exact name of the creator to search for
     * @returns        The number of items by that creator
     */
    public int countCreatorItems(String creator) {
        int counter = 0;
        for (int i = 0; i < pup.size(); i++){
            LibraryItem j = pup.get(i);
            if (j.getCreator() == creator){
                counter ++;
            }
        }
        return counter;
    }

    /* Print all items in the library.
     */
    public void printCollection() {
        for (int i = 0; i < pup.size(); i++){
            LibraryItem f = pup.get(i);
            System.out.println(f.getName() + ", " + f.getAttributionLine());
        }
    }

}