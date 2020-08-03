package {{base_package}}.exceptions;
public class {{entity}}Exception extends WException {


    public {{entity}}Exception() {
        super();
    }

    public {{entity}}Exception(String message) {
        super(message);
    }

    public {{entity}}Exception(String message, Throwable cause) {
        super(message, cause);
    }

    public {{entity}}Exception(Throwable cause) {
        super(cause);
    }

    protected {{entity}}Exception(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}