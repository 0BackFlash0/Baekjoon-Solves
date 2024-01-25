#include <iostream>
using namespace std;

class Array {

private:

    // 멤버 변수
	int* arr; //배열, 이후에 동적할당 할 것
	int arrSize; //배열의 크기


public:

    // Array 생성자
	Array(int size) {
		arrSize = size;
		arr = new int[arrSize]; //size의 크기로 int형 배열 동적할당
		for (int i = 0; i < size; i++) {
			arr[i] = 0;
		}
	}

	// index로 원소에 접근
	int at(int idx) {
		return arr[idx];
	}

    // index에 값을 삽입
	void add(int idx, int value) {
		if (idx > arrSize - 1) {
			cout << -1 << endl; //범위 벗어나면 -1 출력
		}
		else {
			for (int i = arrSize - 2; i >= idx; i--) {
				arr[i + 1] = arr[i];
				//맨 뒤에서 2번째 원소부터 idx번째 원소까지 왼쪽으로 한칸씩 이동
			}
			arr[idx] = value;  //idx번째 원소에 값 대입
		}

	}

	// index의 원소 삭제
	void remove(int idx) {
		for (int i = idx; i < arrSize - 1; i++) { //idx부터 맨뒤에서 2번째 원소까지
			arr[i] = arr[i + 1];            //자신 다음에 있는 원소 자신에게 대입
		}
		arr[arrSize - 1] = 0;   //마지막 원소에 초기값 0 대입
	}

	void set(int idx, int value) { //idx 원소의 값 대치
		arr[idx] = value;
	}

	void print() {  //모든 원소 출력
		for (int i = 0; i < arrSize; i++) {
			cout << arr[i] << " ";
		}
		cout << endl;
	}

};

//int main() {
//	Array ar(5);
//	ar.add(1, 10); //0 10 0 0 0
//	ar.add(1, 20); //0 20 10 0 0
//	ar.print();  //0 20 10 0 0 출력
//
//	ar.remove(1); //0 10 0 0 0
//	ar.print();  //0 10 0 0 0 출력
//
//	ar.remove(1); //0 0 0 0 0
//	ar.print();  //0 0 0 0 0 출력
//
//}
