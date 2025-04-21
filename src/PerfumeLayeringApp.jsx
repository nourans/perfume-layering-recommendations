import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

export default function PerfumeLayeringApp() {
  const [perfumes, setPerfumes] = useState([]);
  const [newPerfume, setNewPerfume] = useState('');
  const [recommendations, setRecommendations] = useState('');
  const [analysis, setAnalysis] = useState('');
  const [loading, setLoading] = useState(false);

  const handleAddPerfume = () => {
    if (newPerfume.trim()) {
      setPerfumes([...perfumes, newPerfume.trim()]);
      setNewPerfume('');
    }
  };

  const handleGetRecommendations = async () => {
    setLoading(true);
    const response = await fetch('/api/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ perfumes })
    });
    const data = await response.json();
    setRecommendations(data.recommendations);
    setLoading(false);
  };

  const handleGetAnalysis = async () => {
    setLoading(true);
    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ perfumes })
    });
    const data = await response.json();
    setAnalysis(data.analysis);
    setLoading(false);
  };

  return (
    <div className="max-w-xl mx-auto py-10 px-4">
      <h1 className="text-2xl font-bold mb-4">Perfume Layering Recommendation System</h1>

      <div className="mb-4">
        <Input
          placeholder="Enter perfume name (e.g. Gucci Flora)"
          value={newPerfume}
          onChange={(e) => setNewPerfume(e.target.value)}
        />
        <Button className="mt-2" onClick={handleAddPerfume}>Add Perfume</Button>
      </div>

      <div className="mb-4">
        <h2 className="font-semibold">Your Collection:</h2>
        <ul className="list-disc ml-5">
          {perfumes.map((p, idx) => <li key={idx}>{p}</li>)}
        </ul>
      </div>

      <div className="space-x-2 mb-6">
        <Button onClick={handleGetRecommendations} disabled={loading}>Get Layering Recommendations</Button>
        <Button onClick={handleGetAnalysis} disabled={loading}>Analyze Collection</Button>
      </div>

      {recommendations && (
        <Card className="mb-4">
          <CardContent>
            <h2 className="font-semibold mb-2">Layering Recommendations:</h2>
            <pre className="whitespace-pre-wrap text-sm">{recommendations}</pre>
          </CardContent>
        </Card>
      )}

      {analysis && (
        <Card>
          <CardContent>
            <h2 className="font-semibold mb-2">Fragrance Analysis:</h2>
            <pre className="whitespace-pre-wrap text-sm">{analysis}</pre>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
