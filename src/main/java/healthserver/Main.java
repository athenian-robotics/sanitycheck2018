package healthserver;

import static spark.Spark.*;
import java.util.Random;
public class Main {
    public static void main(String[] args) {

        Random randomGenerator = new Random();
        get("/gremlin", (req, res) -> Gremlin.getGremlinString());
        String status = "TestFalse: " + GetHealth.checkStatus("TestFalse") + " | TestTrue: " + GetHealth.checkStatus("TestTrue");
        get("/status", (req, res) -> status);
    }
}