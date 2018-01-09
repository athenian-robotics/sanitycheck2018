package healthserver;
//TODO implement status checking by system
class GetHealth {
    static String checkStatus(String system) {
        if (system.contentEquals("TestTrue")) {
            return ("OK");
        } else if (system.contentEquals("TestFalse")) {
            return ("PROBLEM WITH SYSTEM");
        } else {
            return ("UNKNOWN SYSTEM");
        }
    }
}
