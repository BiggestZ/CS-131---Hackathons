public class LibraryItem {

    protected String l_name;
    protected String l_creator;

    public LibraryItem(String name, String creator) {
        setName(name);
        setCreator(creator);
    }

    public String getName() {
        return l_name;
    }

    public void setName(String name) {
        l_name = name;
    }

    public String getCreator() {
        return l_creator;
    }

    public void setCreator(String creator) {
        l_creator = creator;
    }

    public String getAttributionLine() {
        return "created by " + this.getCreator();
    }

}