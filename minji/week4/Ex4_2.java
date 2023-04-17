package org.example.chap4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex4_2 {

	public static boolean check(int h, int m, int s) {
		// h -> 1의 자리가 3, m -> 30이거나 1의 자리가 3, s -> 30이거나 1의 자리가 3
		if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
			return true;
		return false;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		int count = 0;
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j < 60; j++) {
				for (int k = 0; k < 60; k++) {
					// String time = Integer.toString(N).concat(Integer.toString(j)).concat(Integer.toString(k));
					// System.out.println(time);
					// if (time.contains("3")) count++;

					if (check(i, j, k)) count++;
				}
			}
		}

		System.out.println(count);
	}
}
