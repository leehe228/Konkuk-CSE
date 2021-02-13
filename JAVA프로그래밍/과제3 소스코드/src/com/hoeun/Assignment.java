package com.hoeun;

public class Assignment {

	public static void main(String[] args) {
		System.out.println("202011353 이호은 과제3");

		TaxManager seoul = new TaxManager("Seoul", 10);
		seoul.addTaxPayer(new TaxPayer("A", "0001", 2500));
		seoul.addTaxPayer(new SalaryTaxPayer("B", "0002", 4500, "ComA"));
		seoul.addTaxPayer(new SalaryTaxPayer("C", "0003", 6500, "ComB"));
		seoul.addTaxPayer(new SalaryTaxPayer("D", "0004", 8500, "ComC"));
		seoul.addTaxPayer(new SalaryTaxPayer("E", "0005", 300, "ComD"));
		seoul.addTaxPayer(new SalaryTaxPayer("F", "0006", 900, "ComE"));
		seoul.addTaxPayer(new BusinessTaxPayer("G", "0007", 1300, 500));
		seoul.addTaxPayer(new BusinessTaxPayer("H", "0008", 2700, 4000));
		seoul.addTaxPayer(new BusinessTaxPayer("I", "0009", 3200, 100));
		seoul.addTaxPayer(new BusinessTaxPayer("J", "0010", 9200, 3000));
		seoul.addTaxPayer(new BusinessTaxPayer("K", "0011", 3100, 2000));
		seoul.addTaxPayer(new TaxPayer("L", "0012", 1000));

		seoul.showTax();
		seoul.showSalaryTaxPayer();
		seoul.showBusinessTaxPayer();

		TaxManager busan = new TaxManager("Busan", 5);
		busan.addTaxPayer(new TaxPayer("M", "1001", 10000));
		busan.addTaxPayer(new SalaryTaxPayer("N", "1002", 7200, "ComF"));
		busan.addTaxPayer(new SalaryTaxPayer("O", "1003", 3100, "ComG"));
		busan.addTaxPayer(new BusinessTaxPayer("P", "1004", 4500, 500));
		busan.addTaxPayer(new BusinessTaxPayer("Q", "1005", 3000, 2500));

		busan.showTax();
		busan.showSalaryTaxPayer();
		busan.showBusinessTaxPayer();
	}

}
