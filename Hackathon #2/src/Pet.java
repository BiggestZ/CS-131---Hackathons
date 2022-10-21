public class Pet {

    // FIXME member variables here, if necessary
    protected String pName;
    protected String pSpecies;
    /* Constructor; The species of the pet and its name
     *
     * @param species  The species of this pet
     * @param name     The name of this pet
     */

    public Pet(){
    }

    public Pet(String name){ //Used in Duck / Goose classes
        setName(name);
    }

    public Pet(String species, String name) {  // Base Constructor
        setSpecies(species);
        setName(name);
    }

    /* Get the species of this pet
     *
     * @returns  The species of this pet
     */
    public String getSpecies() {
        return pSpecies;
    }

    public void setSpecies(String species) {
        pSpecies = species;
    }
    /* Get the name of this pet
     *
     * @returns  The name of this pet
     */
    public String getName() {
        return pName;
    }

    public void setName(String name) {
        pName = name;
    }

    /* Check whether this pet and the other pet are the same
     *
     * Two pets are the same if they are the same species and have the same name.
     *
     * @param other  The pet to check against.
     * @returns      true if two pets are the same, false otherwise
     */
    public boolean equals(Pet other) {
        if (this.getName() == other.getName() && this.getSpecies() == other.getSpecies()){
            return true;
        } else {
            return false;
        }

    }

    /* Print "I love the Beach Boys!".
     */
    public void makeSound() {
        System.out.println("I love the Beach Boys!");
        // FIXME your code here
    }
}
