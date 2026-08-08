-- 1. DIMENSION SYMBOL

CREATE TABLE IF NOT EXISTS dim_symbol(
    symbol_id BIGINT PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL UNIQUE
);


--2. DIMENSION FINANCIAL CONCEPT

CREATE TABLE IF NOT EXISTS dim_financial_concept(
    concept_id BIGINT PRIMARY KEY,
    statement_type VARCHAR(5) NOT NULL,
    concept TEXT NOT NULL,
    label TEXT NOT NULL,

    CONSTRAINT uq_financial_concept
    UNIQUE (statement_type,concept),
    CONSTRAINT chk_statement_type
    CHECK (statement_type IN ('BS','CF','IC'))
);

--3. FACT BALANCE SHEET

CREATE TABLE IF NOT EXISTS fact_financial_bs(
    symbol_id BIGINT NOT NULL,
    concept_id BIGINT NOT NULL,
    year INTEGER NOT NULL,
    quarter  integer not null,
    value NUMERIC(30,6),
    unit VARCHAR(100),

    CONSTRAINT fk_bs_symbol
    FOREIGN KEY (symbol_id)
    REFERENCES dim_symbol(symbol_id),

    CONSTRAINT fk_bs_concept
    FOREIGN KEY (concept_id)
    REFERENCES dim_financial_concept(concept_id),

    CONSTRAINT chk_bs_quarter
    CHECK (quarter BETWEEN 0 AND 4)
);

--4. FACT CASH FLOW

CREATE TABLE IF NOT EXISTS fact_financial_cf(
     symbol_id BIGINT NOT NULL,
    concept_id BIGINT NOT NULL,
    year INTEGER NOT NULL,
    quarter  integer not null,
    value NUMERIC(30,6),
    unit VARCHAR(100),

    CONSTRAINT fk_cf_symbol
    FOREIGN KEY (symbol_id)
    REFERENCES dim_symbol(symbol_id),

    CONSTRAINT fk_cf_concept
    FOREIGN KEY (concept_id)
    REFERENCES dim_financial_concept(concept_id),

    CONSTRAINT chk_cf_quarter
    CHECK (quarter BETWEEN 0 AND 4)
);

--5. FACT INCOME STATEMENT

CREATE TABLE IF NOT EXISTS fact_financial_ic(
     symbol_id BIGINT NOT NULL,
    concept_id BIGINT NOT NULL,
    year INTEGER NOT NULL,
    quarter  integer not null,
    value NUMERIC(30,6),
    unit VARCHAR(100),

    CONSTRAINT fk_ic_symbol
    FOREIGN KEY (symbol_id)
    REFERENCES dim_symbol(symbol_id),

    CONSTRAINT fk_ic_concept
    FOREIGN KEY (concept_id)
    REFERENCES dim_financial_concept(concept_id),

    CONSTRAINT chk_ic_quarter
    CHECK (quarter BETWEEN 0 AND 4)
);


--6. FACT CANDLES

CREATE TABLE IF NOT EXISTS fact_candles(
    symbol_id BIGINT NOT NULL,
    trade_date DATE NOT NULL,
    open NUMERIC(20,6),
    high NUMERIC(20,6),
    low NUMERIC(20,6),
    close NUMERIC(20,6),
    volume BIGINT,
    price_change NUMERIC(20,6),
    price_change_pct NUMERIC(12,4),
    daily_change NUMERIC(20,6),
    daily_change_pct NUMERIC(12,4),
    previous_volume BIGINT,
    volume_change_pct NUMERIC(12,4),

    CONSTRAINT fk_candles_symbol
    FOREIGN KEY (symbol_id)
    REFERENCES dim_symbol(symbol_id)
);

--7. FACT EARNING

CREATE TABLE IF NOT EXISTS fact_earnings (
    symbol_id BIGINT NOT NULL,

    year INTEGER,
    quarter INTEGER,
    period VARCHAR(20),

    actual_eps NUMERIC(20,6),
    estimated_eps NUMERIC(20,6),

    eps_surprise NUMERIC(20,6),
    surprise_percent NUMERIC(12,4),

    eps_beat_miss VARCHAR(10),
    eps_surprise_abs NUMERIC(20,6),

    fiscal_year_quarter VARCHAR(10),

    CONSTRAINT fk_earnings_symbol
        FOREIGN KEY (symbol_id)
        REFERENCES dim_symbol(symbol_id)
);

-- DIM NEWS 
CREATE TABLE IF NOT EXISTS dim_news (
    news_id BIGINT PRIMARY KEY,

    symbol_id BIGINT,

    category VARCHAR(100),
    headline TEXT,
    summary TEXT,

    source VARCHAR(255),
    article_url TEXT,

    published_at TIMESTAMP,

    CONSTRAINT fk_news_symbol
        FOREIGN KEY (symbol_id)
        REFERENCES dim_symbol(symbol_id)
);

--DIM COMPANY
CREATE TABLE IF NOT EXISTS dim_company (
    symbol_id BIGINT PRIMARY KEY,

    company_name VARCHAR(255),
    country VARCHAR(100),
    currency VARCHAR(20),
    estimate_currency VARCHAR(20),
    exchange VARCHAR(100),
    industry VARCHAR(255),

    floating_share NUMERIC(20,4),
    ipo_date DATE,

    logo_url TEXT,
    market_cap NUMERIC(30,2),
    phone VARCHAR(50),
    shares_outstanding NUMERIC(30,2),

    website TEXT,
    processed_at TIMESTAMP,

    CONSTRAINT fk_company_symbol
        FOREIGN KEY (symbol_id)
        REFERENCES dim_symbol(symbol_id)
);

--FACT MARKET STATUS
CREATE TABLE IF NOT EXISTS fact_market (
    market_id BIGSERIAL PRIMARY KEY,

    exchange VARCHAR(50),
    holiday VARCHAR(100),
    is_open BOOLEAN,
    session VARCHAR(30),

    market_time TIMESTAMP,
    timezone VARCHAR(50),

    market_status VARCHAR(20),
    is_regular_session BOOLEAN,

    market_date DATE,
    market_year INTEGER,
    market_month INTEGER,
    market_quarter INTEGER,
    market_day INTEGER,
    market_hour INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--.  INDEXES
-- BALANCE SHEET
CREATE INDEX IF NOT EXISTS idx_bs_symbol
ON fact_financial_bs(symbol_id);

CREATE INDEX IF NOT EXISTS idx_bs_concept
ON fact_financial_bs(concept_id);

CREATE INDEX IF NOT EXISTS idx_bs_year_quarter
ON fact_financial_bs(year,quarter);

-- CASH FLOW
CREATE INDEX IF NOT EXISTS idx_cf_symbol
ON fact_financial_cf(symbol_id);

CREATE INDEX IF NOT EXISTS idx_cf_concept
ON fact_financial_cf(concept_id);

CREATE INDEX IF NOT EXISTS idx_cf_year_quarter
ON fact_financial_cf(year,quarter);

--  INCOME STATEMENT
CREATE INDEX IF NOT EXISTS idx_ic_symbol
ON fact_financial_ic(symbol_id);

CREATE INDEX IF NOT EXISTS idx_ic_concept
ON fact_financial_ic(concept_id);

CREATE INDEX IF NOT EXISTS idx_ic_year_quarter
ON fact_financial_ic(year,quarter);

-- FACT CANDLES
CREATE INDEX IF NOT EXISTS idx_candles_symbol_date
ON fact_candles(symbol_id,trade_date);

--FACT EARNINGS

CREATE INDEX IF NOT EXISTS idx_earnings_symbol_year_quarter
ON fact_earnings(symbol_id,year,quarter);

-- NEWS INDEX
CREATE INDEX IF NOT EXISTS idx_news_symbol
ON dim_news(symbol_id);

CREATE INDEX IF NOT EXISTS idx_news_published_at
ON dim_news(published_at);

CREATE INDEX IF NOT EXISTS idx_news_category
ON dim_news(category);

-- COMPANY INDEX
CREATE INDEX IF NOT EXISTS idx_company_industry
ON dim_company(industry);

CREATE INDEX IF NOT EXISTS idx_company_exchange
ON dim_company(exchange);

-- MARKET STATUS INDEX
CREATE INDEX IF NOT EXISTS idx_fact_market_date
ON fact_market(market_date);

CREATE INDEX IF NOT EXISTS idx_fact_market_exchange
ON fact_market(exchange);

CREATE INDEX IF NOT EXISTS idx_fact_market_time
ON fact_market(market_time);
