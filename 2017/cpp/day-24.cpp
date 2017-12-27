#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct port
{
	int end1;
	int end2;
};

// InputReader
//~~~~~~~~~~~~~~
class InputReader
{
	string path;

public:
	InputReader(string _path)
	{
		path = _path;
	}
	vector<port> ports();
};

vector<port> InputReader::ports()
{
	ifstream input(path);
	vector<port> output;
	string tmp;
	vector<port> ports;
	while (getline(input, tmp))
	{
		port t;
		t.end1 = stoi(tmp.substr(0));
		t.end2 = stoi(tmp.substr(tmp.find('/') + 1));
		ports.push_back(t);
	}
	return ports;
}

// BridgeBuilder
//~~~~~~~~~~~~~~
class BridgeBuilder
{
	vector<port> start;
	vector<port> ports;
	vector<vector<port>> buildAllBridgesRecursive(vector<port> &prev, vector<port> &ports);

public:
	BridgeBuilder(vector<port> _ports)
	{
		ports = _ports;
		port startPort;
		startPort.end1 = 0;
		startPort.end2 = 0;
		start.push_back(startPort);
	}
	vector<vector<port>> buildAllBridges();
};

vector<vector<port>> BridgeBuilder::buildAllBridges()
{
	return buildAllBridgesRecursive(start, ports);
}

vector<vector<port>> BridgeBuilder::buildAllBridgesRecursive(vector<port> &bridge, vector<port> &ports)
{
	vector<vector<port>> bridges;
	port lastPort = bridge[bridge.size() - 1];
	bool noMatch = true;

	for (int i = 0; i < ports.size(); i++)
	{
		port current = ports[i];

		if (lastPort.end2 == current.end1 || lastPort.end2 == current.end2)
		{
			noMatch = false;
			port portToPush;
			vector<port> nextBridge;
			vector<port> nextPorts;
			if (lastPort.end2 == current.end1)
			{
				portToPush.end1 = current.end1;
				portToPush.end2 = current.end2;
			}
			else
			{
				portToPush.end1 = current.end2;
				portToPush.end2 = current.end1;
			}
			for (int j = 0; j < bridge.size(); j++)
			{
				nextBridge.push_back(bridge[j]);
			}
			nextBridge.push_back(portToPush);
			for (int j = 0; j < ports.size(); j++)
			{
				if (j != i)
				{
					nextPorts.push_back(ports[j]);
				}
			}
			vector<vector<port>> nextBridges = buildAllBridgesRecursive(nextBridge, nextPorts);
			for (int j = 0; j < nextBridges.size(); j++)
			{
				bridges.push_back(nextBridges[j]);
			}
		}
	}

	if (noMatch == true)
	{
		bridges.push_back(bridge);
	}

	return bridges;
}

int main()
{
	InputReader reader("2017/input/day-24.input");
	vector<port> ports = reader.ports();

	BridgeBuilder bridgeBuilder(ports);
	vector<vector<port>> bridges = bridgeBuilder.buildAllBridges();

	int maxSum = 0;
	vector<port> maxBridge;
	for (vector<vector<port>>::iterator bridgeIter = bridges.begin(); bridgeIter != bridges.end(); ++bridgeIter)
	{
		int sum = 0;
		for (vector<port>::iterator portItem = (*bridgeIter).begin(); portItem != (*bridgeIter).end(); ++portItem)
			sum += (*portItem).end1 + (*portItem).end2;
		if ((*bridgeIter).size() > maxBridge.size() ||
				((*bridgeIter).size() == maxBridge.size() && sum > maxSum))
		{
			maxSum = sum;
			maxBridge = *bridgeIter;
		}
	}
	cout << maxSum;
	return 0;
}