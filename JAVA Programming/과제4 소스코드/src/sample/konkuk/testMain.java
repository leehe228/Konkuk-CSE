package sample.konkuk;

public class testMain {

	public static void main(String[] args) {
		System.out.println("202011353 이호은");
		
		VocManager vocManager = new VocManager("이호은");
		vocManager.makeVoc("quiz.txt");
	}
}
