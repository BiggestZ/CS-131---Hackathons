public class Book extends LibraryItem {

    public Book(String name, String creator) {
        super(name, creator);
        if(creator == ""){
            l_creator = "Anonymous";
        }
    }

    public String getAttributionLine() {
        return "written by " + this.getCreator();
    }
    // FIXME function(s) that deal with anonymous authors

}