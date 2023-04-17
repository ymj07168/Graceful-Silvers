package org.example.chap4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex4_2 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		int count = 0;
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j < 60; j++) {
				for (int k = 0; k < 60; k++) {
					String time = Integer.toString(i).concat(Integer.toString(j)).concat(Integer.toString(k));
					if (time.contains("3")) count++;
				}
			}
		}

		System.out.println(count);
	}
}
