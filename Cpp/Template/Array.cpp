#include <iostream>
using namespace std;

class Array {

private:

    // ��� ����
	int* arr; //�迭, ���Ŀ� �����Ҵ� �� ��
	int arrSize; //�迭�� ũ��


public:

    // Array ������
	Array(int size) {
		arrSize = size;
		arr = new int[arrSize]; //size�� ũ��� int�� �迭 �����Ҵ�
		for (int i = 0; i < size; i++) {
			arr[i] = 0;
		}
	}

	// index�� ���ҿ� ����
	int at(int idx) {
		return arr[idx];
	}

    // index�� ���� ����
	void add(int idx, int value) {
		if (idx > arrSize - 1) {
			cout << -1 << endl; //���� ����� -1 ���
		}
		else {
			for (int i = arrSize - 2; i >= idx; i--) {
				arr[i + 1] = arr[i];
				//�� �ڿ��� 2��° ���Һ��� idx��° ���ұ��� �������� ��ĭ�� �̵�
			}
			arr[idx] = value;  //idx��° ���ҿ� �� ����
		}

	}

	// index�� ���� ����
	void remove(int idx) {
		for (int i = idx; i < arrSize - 1; i++) { //idx���� �ǵڿ��� 2��° ���ұ���
			arr[i] = arr[i + 1];            //�ڽ� ������ �ִ� ���� �ڽſ��� ����
		}
		arr[arrSize - 1] = 0;   //������ ���ҿ� �ʱⰪ 0 ����
	}

	void set(int idx, int value) { //idx ������ �� ��ġ
		arr[idx] = value;
	}

	void print() {  //��� ���� ���
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
//	ar.print();  //0 20 10 0 0 ���
//
//	ar.remove(1); //0 10 0 0 0
//	ar.print();  //0 10 0 0 0 ���
//
//	ar.remove(1); //0 0 0 0 0
//	ar.print();  //0 0 0 0 0 ���
//
//}
