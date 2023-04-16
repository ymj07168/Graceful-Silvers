package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Ex3_3 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[][] cards = new int[N][M];
		int[] mins = new int[N];
		for (int i = 0; i < N; i++) {
			int min = 100;
			for (int j = 0; j < M; j++) {
				cards[i][j] = Integer.parseInt(st.nextToken());
				if (cards[i][j] < min) min = cards[i][j];
			}
			mins[i] = min;
		}

		Arrays.sort(mins);
		System.out.println(mins[N-1]);


	}
}
