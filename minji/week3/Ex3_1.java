package org.example;

public class Ex3_1 {

	public static void main(String[] args) {

		/* 나동빈님 코드 */
		int n  = 1260;
		int count = 0;

		int[] coin_types = {500, 100, 50, 10};

		for (int i = 0; i < coin_types.length; i++) {
			count += n / coin_types[i];
			n %= coin_types[i];
		}

		System.out.println(count);


		/* 내가 원래 생각한 코드 */
		// count += n / 500;
		// n %= 500;
		//
		// count += n / 100;
		// n %= 100;
		//
		// count += n / 50;
		// n %= 50;
		//
		// count += n / 10;

	}
}
