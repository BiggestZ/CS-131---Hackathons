import java.util.ArrayList;
public class PetHotel {

    // FIXME member variables here, if necessary
    public int num_rooms;
    public int room_avail;
    private ArrayList<Pet> petz; 

    /* Constructor; creates a hotel with numRooms of rooms with all rooms unoccupied
     *
     * @param numRooms  The number of rooms in this hotel
     */
    public PetHotel(int numRooms) {
        this.num_rooms = numRooms;
        this.petz = new ArrayList<Pet>(num_rooms); //Sets length of ArrayList to # rooms
        this.room_avail = numRooms;
    }

    /* Get the number of unoccupied rooms in this hotel
     *
     * @returns  The number of unoccupied rooms in this hotel
     */
    public int numRoomsAvailable() { 
        // Works
        return room_avail;
    }

    /* Check in a pet
     *
     * A pet will always get the empty room with the lowest room number
     *
     * @param pet  The pet going to be checked in
     * @returns    true if there is an empty room for the pet, false otherwise
     */
    public boolean checkIn(Pet pet) {
        if (room_avail == 0) { //Checks in pet, if a room is available
            //Works!
            return false;
        } else {
            // Works!
            petz.add(pet); //Add from 1st element down
            room_avail--;
            return true; 
        }
    }

    /* Check out a pet
     *
     * The room that was occupied by this pet becomes empty
     *
     * @param pet  The pet going to be checked out
     * @returns    true if the pet is staying at the hotel (and so can successfully check out),
     *             and returns false otherwise.
     */
    public boolean checkOut(Pet pet) {
        if (petz.contains(pet)){
            // Works!
            petz.remove(pet);
            room_avail++;
            return true;
        } else {
            // Works!
            return false;
        } 
    }
    /* Get the occupant of a particular room
     *
     * If an invalid roomNumber is given, this function should return null
     *
     * @param roomNumber  The roomNumber of the room to examine
     * @returns           The pet that occupies room roomNumber;
     *                    return null if roomNumber is invalid
     */
    public Pet getOccupantOf(int roomNumber) {
        if (roomNumber > num_rooms || roomNumber < 0){ //Check if number exists
            // Works!
            System.out.println("LOLZ");
            return null;
        } else {
            // Works!
            return petz.get(roomNumber); //If # exists, returns item at index
        }
    }

    /* Get the room of a specific pet
     *
     * If the pet is not staying at this hotel, this function should return -1
     *
     * @param pet  The pet to look for
     * @returns    The room number of the room that the specific pet occupies;
     *             return -1 is the pet is not staying at the this hotel
     */

    public int getRoomOf(Pet pet) {
        for(int i = 0; i < num_rooms;i++){
            if (petz.get(i) == pet){
                return i;
            } 
        } 
        System.out.println("STAY MAD");
        return -1; //Shows the pet is not registered to hotel
    }
}