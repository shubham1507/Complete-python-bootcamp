const handleSearch = async (data) => {
  try {
    setLoading(true);

    // Fetch response using run_id (your existing API)
    const response = await apiClient.get(
      /api/v1/services/test_run/domains/${domainName}/projects/${projectName}/test-runs?run_id=${data.testRunId}
    );

    let results = response.data.data; // all runs from backend
    let filteredResults = results;

    // If user entered runName (frontend search)
    if (data.runName && data.runName.trim() !== "") {
      filteredResults = results.filter(run =>
        run.run_name.toLowerCase().includes(data.runName.toLowerCase())
      );
    }

    setRuns(filteredResults);
    setTotalRows(filteredResults.length);
  } catch (error) {
    if (error.response?.status === 401) {
      logout(true);
    } else if (error.response?.status === 403) {
      console.error(Access denied for project ${projectName});
    } else {
      console.error("Error fetching data: ", error.message);
    }
  } finally {
    setLoading(false);
  }
};
