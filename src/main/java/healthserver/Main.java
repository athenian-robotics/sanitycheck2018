package healthserver;

import static spark.Spark.*;
import java.util.Random;
public class Main {
    public static void main(String[] args) {
        String[] strs = new String[18];
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
        strs[10] = "Developing anti-Elf weapons...";
        strs[11] = "Editing history to brainwash population...";
        strs[12] = "Mourning the death of Papa Gremlin...";
        strs[13] = "Gremlins rally in the streets around Elf hate...";
        strs[14] = "Production delayed from Elf attacks...";
        strs[15] = "Gremlin widows mourn...";
        strs[16] = "Introducing new taxes to pay for war...";
        strs[17] = "Gremlin warchief dies heroically during tactical retreat...";
        Random randomGenerator = new Random();
        get("/gremlin", (req, res) -> strs[randomGenerator.nextInt(strs.length)]);
        String status = "TestFalse: " + GetHealth.checkStatus("TestFalse") + " | TestTrue: " + GetHealth.checkStatus("TestTrue");
        get("/status", (req, res) -> status);
    }
}