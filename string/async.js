const handleSearch = async (data) => {
  try {
    setLoading(true);

    // fetch using your existing run_id API
    const res = await apiClient.get(
      `/api/v1/services/test_run/domains/${domainName}/projects/${projectName}/test-runs?run_id=${data.testRunId}`
    );

    const results = res.data?.data ?? [];
    const filtered = data.runName
      ? results.filter(r =>
          (r.run_name || "").toLowerCase().includes(data.runName.toLowerCase())
        )
      : results;

    setRuns(filtered);
    setTotalRows(filtered.length);
  } catch (err) {
    if (err.response?.status === 401) logout(true);
    else if (err.response?.status === 403) {
      console.error(`Access to project ${projectName} denied: ${err.message}`);
    } else {
      console.error(`Error fetching data: ${err.message}`);
    }
  } finally {
    setLoading(false);
  }
};
