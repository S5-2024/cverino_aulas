import java.util.Locale;
import java.util.Scanner;

public class CalculoSimples {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);
    double[] peca1 = new double[3];
    double[] peca2 = new double[3];

    for (int i = 0; i < peca1.length; i++) {
      peca1[i] = sc.nextDouble();
    }
    for (int i = 0; i < peca2.length; i++) {
      peca2[i] = sc.nextDouble();
    }
    double valor = peca1[1] * peca1[2];
    double valor2 = peca2[1] * peca2[2];
    double total = valor + valor2;
    System.out.printf("VALOR A PAGAR: R$ %.2f%n",total);
    sc.close();

  }

}
