import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import QuotaPage from '@/app/(dashboard)/settings/quotas/page';

vi.mock('@/lib/api', () => ({
  getWorkspaceQuotaPolicies: vi.fn(),
  setWorkspaceQuotaPolicy: vi.fn(),
}));

describe('QuotaPage', () => {
  it('loads quota policies and renders table', async () => {
    const { getWorkspaceQuotaPolicies } = await import('@/lib/api');
    vi.mocked(getWorkspaceQuotaPolicies).mockResolvedValue([
      {
        feature_class: 'qa_synthesis',
        user_class: 'vip',
        limit: 500,
        window_seconds: 86400,
      },
    ]);

    render(<QuotaPage />);

    expect(screen.getByText(/loading/i)).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByText(/qa_synthesis/i)).toBeInTheDocument();
    });
  });

  it('shows error state if API fails', async () => {
    const { getWorkspaceQuotaPolicies } = await import('@/lib/api');
    vi.mocked(getWorkspaceQuotaPolicies).mockRejectedValue(new Error('boom'));

    render(<QuotaPage />);

    await waitFor(() => {
      expect(screen.getByText(/error/i)).toBeInTheDocument();
    });
  });

  it('submits a new policy', async () => {
    const user = userEvent.setup();
    const { getWorkspaceQuotaPolicies, setWorkspaceQuotaPolicy } = await import('@/lib/api');

    vi.mocked(getWorkspaceQuotaPolicies).mockResolvedValue([]);
    vi.mocked(setWorkspaceQuotaPolicy).mockResolvedValue({
      feature_class: 'qa_synthesis',
      user_class: 'vip',
      limit: 500,
      window_seconds: 86400,
    });

    render(<QuotaPage />);

    await user.selectOptions(screen.getByRole('combobox', { name: /user class/i }), 'vip');
    await user.selectOptions(screen.getByRole('combobox', { name: /feature class/i }), 'qa_synthesis');
    await user.type(screen.getByRole('spinbutton', { name: /limit/i }), '500');
    await user.type(screen.getByRole('spinbutton', { name: /window/i }), '86400');
    await user.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(setWorkspaceQuotaPolicy).toHaveBeenCalled();
    });
  });
});