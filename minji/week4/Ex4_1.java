package org.example.chap4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Ex4_1 {
	public static void main(String[] args) throws IOException {
		int x = 1, y = 1;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());

		while (st.hasMoreTokens()) {
			String dir = st.nextToken();

			if ("L".equals(dir)) y -= 1;
			else if ("R".equals(dir)) y += 1;
			else if ("U".equals(dir)) x -= 1;
			else if ("D".equals(dir)) x += 1;

			if (x < 1) x += 1;
			else if (x > N) x -= 1;
			else if (y < 1) y += 1;
			else if (y > N) y -= 1;
		}

		System.out.println(x + " " + y);
	}
}
