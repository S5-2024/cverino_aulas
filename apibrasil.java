import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.net.ssl.HttpsURLConnection;

public class apibrasil {
  @SuppressWarnings("deprecation")
  public static void main(String[] args) {
    try {
        String cnpj = "18.715.508/0001-31";
        cnpj = cnpj.replace("/", "").replace(".","").replace("-","");
        String url = "https://brasilapi.com.br/api/cnpj/v1/" + cnpj;

        HttpURLConnection  connection = (HttpsURLConnection) new URL(url).openConnection();
        connection.setRequestMethod("GET");

        int responseCode = connection.getResponseCode();

        if(responseCode == HttpURLConnection.HTTP_OK){
          BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
          String inputLine;
          StringBuilder response = new StringBuilder();

          while((inputLine = in.readLine()) !=null){
            response.append(inputLine);
          }
          in.close();
          
          System.out.println("Responsta da API: ");
          System.out.println(response.toString());

        }else{
          System.out.println("Erro na requisição. Código de resposta: " + responseCode);
        }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
