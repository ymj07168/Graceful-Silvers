package org.example.chap4;

import java.util.Scanner;

public class Ex4_3 {		// 왕실의 나이트
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String pos = sc.nextLine();
		int x = pos.charAt(0);
		int y = Integer.parseInt(String.valueOf(pos.charAt(1)));
		int count = 0;

		if (x + 2 < 105 && y + 1 < 9) count++;
		if (x + 2 < 105 && y - 1 > 0) count++;
		if (x - 2 > 96 && y + 1 < 9) count++;
		if (x - 2 > 96 && y - 1 > 0) count++;
		if (x + 1 < 105 && y + 2 < 9) count++;
		if (x + 1 < 105 && y - 2 > 0) count++;
		if (x - 1 > 96 && y + 2 < 9) count++;
		if (x - 1 > 96 && y - 2 > 0) count++;

		System.out.println(count);

	}
}
