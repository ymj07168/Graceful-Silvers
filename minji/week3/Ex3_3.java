package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Ex3_3 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int max = 0;
		for (int i = 0; i < N; i++) {
			int min = 10001;
			for (int j = 0; j < M; j++) {
				int num = Integer.parseInt(st.nextToken());
				if (num < min) min = num;
			}
			if (min > max) max = min;
		}

		System.out.println(max);
	}
}
