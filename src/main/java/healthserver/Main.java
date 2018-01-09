package healthserver;

import healthserver.GetHealth;

import static spark.Spark.*;
import java.util.Random;
public class Main {
    public static void main(String[] args) {
        String[] strs = new String[10];
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
        Random randomGenerator = new Random();
        get("/gremlin", (req, res) -> strs[randomGenerator.nextInt(10)]);
        String status = "TestFalse: " + GetHealth.checkStatus("TestFalse") + " | TestTrue: " + GetHealth.checkStatus("TestTrue");
        get("/status", (req, res) -> status);
    }
}