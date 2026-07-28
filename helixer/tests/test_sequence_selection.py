import pytest

from helixer.core.sequence_selection import parse_manifest, read_fasta, write_report, write_selected_fasta


def write(path, text):
    path.write_text(text, encoding='utf-8')
    return str(path)


def test_selected_fasta_preserves_order_identifiers_and_sequences(tmp_path):
    fasta = write(tmp_path / 'input.fa', '>first description\nACGT\n>second\nTT\n')
    manifest = write(tmp_path / 'selection.tsv', 'seqid\tinclude\treason\nfirst\tfalse\tshort\nsecond\ttrue\tkeep\n')
    records = read_fasta(fasta)
    decisions = parse_manifest(manifest, records)
    selected = tmp_path / 'selected.fa'
    write_selected_fasta(selected, records, decisions)
    assert selected.read_text() == '>second\nTT\n'
    report = tmp_path / 'report.tsv'
    write_report(report, records, decisions, 4, manifest)
    text = report.read_text()
    assert 'full_two_strand_fixed_window_rows\t4' in text
    assert 'selected_two_strand_fixed_window_rows\t2' in text
    assert 'selected_padded_positions\t8' in text


@pytest.mark.parametrize('manifest, message', [
    ('seqid\tinclude\na\ttrue\na\tfalse\nb\ttrue\n', 'duplicate'),
    ('seqid\tinclude\na\ttrue\n', 'no decision'),
    ('seqid\tinclude\na\tyes\nb\ttrue\n', 'invalid include'),
    ('seqid\tinclude\na\tfalse\nb\tfalse\n', 'excludes every'),
    ('seqid\tinclude\na\ttrue\nunknown\tfalse\nb\ttrue\n', 'absent'),
])
def test_manifest_rejects_unsafe_decisions(tmp_path, manifest, message):
    records = read_fasta(write(tmp_path / 'input.fa', '>a\nA\n>b\nT\n'))
    path = write(tmp_path / 'selection.tsv', manifest)
    with pytest.raises(ValueError, match=message):
        parse_manifest(path, records)
