from runova_mesh.probe import collect_probe


def test_collect_probe_has_expected_shape() -> None:
    result = collect_probe()
    assert result["hostname"]
    assert "cpu" in result
    assert "memory" in result
    assert isinstance(result["gpu"], list)
    assert result["gpu_count"] == len(result["gpu"])
    assert result["vram_total_mib"] >= 0
