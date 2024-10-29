import java.util.Locale;
import java.util.Scanner;

public class Esfera {
  public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);
    double R = sc.nextDouble();
    double volume = (4.0 / 3) * 3.14159 * Math.pow(R, 3);

    System.out.printf("VOLUME = %.3f%n", volume);

  }
}
