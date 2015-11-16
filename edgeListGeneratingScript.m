OLEdge = struct2array(tdfread('OLedge.txt'));
OLNode = struct2array(tdfread('OLnode.txt'));

SJEdge = struct2array(tdfread('SJedge.txt'));
SJNode = struct2array(tdfread('SJnode.txt'));

SFEdge = struct2array(tdfread('SFedge.txt'));
SFNode = struct2array(tdfread('SFnode.txt'));

lambdaVec = [0.001, 0.01, 0.1];
for ind = 1:length(lambdaVec);
    ind
    newEdgeList = computeModelEdgeList(size(OLNode,1), OLEdge, 'MDS', lambdaVec(ind));
    fname = strcat('modelOLEdges_lambda', num2str(ind), '.txt'); 
    dlmwrite(fname, newEdgeList, 'delimiter', '\t');
    
    a = 'finished OL'
    
%     newEdgeList = computeModelEdgeList(size(SFNode,1), SFEdge, 'MDS', lambdaVec(ind));
%     fname = strcat('modelSFEdges_lambda', num2str(ind), '.txt'); 
%     dlmwrite(fname, newEdgeList, 'delimiter', '\t');
%     a = 'finished SF'
end
for ind = 1:length(lambdaVec);
    ind
    newEdgeList = computeModelEdgeList(size(SJNode,1), SJEdge, 'MDS', lambdaVec(ind));
    fname = strcat('modelSJEdges_lambda', num2str(ind), '.txt'); 
    dlmwrite(fname, newEdgeList, 'delimiter', '\t');
    a = 'finished SJ'
end
