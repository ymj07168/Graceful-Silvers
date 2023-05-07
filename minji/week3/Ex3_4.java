package org.example;

import java.io.*;
import java.util.*;

public class Ex3_4 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int count = 0;

		while (N >= K) {
			count += N - (N/K)*K;
			N = (N/K)*K;

			N /= K;
			count++;
		}

		System.out.println(count + (N-1));
	}
}
