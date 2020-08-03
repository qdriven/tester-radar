package {{test_package}}.apis;

import {{test_package}}.tc.assertions.URCPAssertion;
import {{test_package}}.tc.requests.LoginRequest;
import {{base_package}}.testing.base.core.WBaseAPITest;
import {{base_package}}.testing.base.core.data.ApiExpResponse;
import {{base_package}}.testing.base.core.data.ApiRequestData;
import {{base_package}}.testing.base.core.data.factory.testng.ApiTestNGDataFactory;
import {{base_package}}.testing.base.core.model.testcase.TestCaseDesc;
import io.restassured.response.Response;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.lang.reflect.Method;
import java.util.Iterator;


public class {{api_name}}ApiTest extends WBaseAPITest{

    @DataProvider(name = "{{api_name}}Data")
    public Iterator<Object[]> getHelloTestCase(Method method) {
        return ApiTestNGDataFactory.defaultApiTestNGData("tc/{{api_name}}.xls");
    }


    @Test(dataProvider = "{{api_name}}Data")
    public void test{{api_name}}Test(ApiRequestData data, TestCaseDesc desc,
                                     ApiExpResponse expResponse,String count,
                                     String param1,String param2) {

        {{api_name}} request = new {{api_name}}();
        {{api_name}}Api api = new {{api_name}}Api();

        int loopCount = Integer.parseInt(count);
        Response response={{apiCallerName}}ApiCaller.call(api,request,loopCount,param1,param2);

    }

}