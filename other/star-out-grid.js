function starOutGrid(grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === '*') {
                grid[i] = grid[i].map(ele => '%');

                for (let k = 0; k < grid.length; k++) {
                    grid[k][j] = '%';
                }
            }
        }
    }
    grid = grid.map(row => row.map(ele => ele === '%' ? '*' : ele))
    return grid;
}
