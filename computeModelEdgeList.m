function [ newEdgeList ] = computeModelEdgeList( numNodes, edgeListOriginal, dimRedMethod, lambda)
    G = sparse(numNodes,numNodes);
    for ind = 1:size(edgeListOriginal,1)
        G(edgeListOriginal(ind,2)+1,edgeListOriginal(ind,3)+1) = edgeListOriginal(ind,4);
        G(edgeListOriginal(ind,3)+1,edgeListOriginal(ind,2)+1) = edgeListOriginal(ind,4);
    end


    distMat = graphallshortestpaths(G);

    %if strcmp(dimRedMethod, 'MDS')
    lowDimCoords = mdscale(distMat,2);
    D = squareform(pdist(lowDimCoords));
    %end

    P = 1./(1+exp(lambda.*D));
    P = P - diag(diag(P));
    V = triu(P);
    weights = V(:);
    tempVec = ones(length(weights),1);
    [~, idx] = datasample(tempVec, size(edgeListOriginal,1), 'Replace', false, 'Weights', weights);
    adjVec = zeros(length(weights), 1);
    adjVec(idx) = 1;
    adjMat = reshape(adjVec,numNodes, numNodes);
    weightedAdj = adjMat .* D;
    newEdgeList = nan(size(edgeListOriginal,1), 3);
    ctr = 1;
    for i = 1:numNodes
        for j = i+1:numNodes
            if weightedAdj(i,j) > 0;
                newEdgeList(ctr, 1) = i;
                newEdgeList(ctr, 2) = j;
                newEdgeList(ctr, 3) = weightedAdj(i,j);
                ctr = ctr + 1;
            end
        end
    end
end


