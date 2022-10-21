public class Film extends LibraryItem {

    public Film(String name, String creator) {
        super(name,creator);
    }

    public String getAttributionLine() {
        return "directed by " + this.getCreator();
    }

}