package healthserver;

import java.util.Random;

public class Gremlin {

    static String getGremlinString(){
        String[] strs = new String[12];
        strs[0] = "Happy Gremlin and Sad Gremlin are arguing about the war...";
        strs[1] = "Gremlin down! Gremlin Down! Training new Gremlin...";
        strs[2] = "Extracting Gremlins from the pipeline...";
        strs[3] = "Starting Gremlin breeding program...";
        strs[4] = "Training Gremlins for war...";
        strs[5] = "CONSTRUCTING ADDITIONAL PYLONS...";
        strs[6] = "Fighting in Elves in the streets...";
        strs[7] = "Declaring war on the Elvish kingdoms...";
        strs[8] = "Sending scouts through the tunnels...";
        strs[9] = "Building Gremlin Launchers...";
        strs[10] = "Developing anit-Elf weapons...";
        strs[11] = "Editing history to brainwash population...";
        Random randomGenerator = new Random();
        return(strs[randomGenerator.nextInt(strs.length)]);
    }
}
