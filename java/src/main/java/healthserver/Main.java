package healthserver;

import static spark.Spark.*;
public class Main {
    public static void main(String[] args) {
        port(852);
        get("/gremlin", (req, res) -> Gremlin.getGremlinString());
        String status = "TestFalse: " + GetHealth.checkStatus("TestFalse") + " | TestTrue: " + GetHealth.checkStatus("TestTrue");
        get("/status", (req, res) -> status);

    }
}